import tictactoe
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, CallbackQueryHandler


def board():
    return [
        [InlineKeyboardButton(tictactoe.board[0][0], callback_data="00"),
         InlineKeyboardButton(tictactoe.board[0][1], callback_data="01"),
         InlineKeyboardButton(tictactoe.board[0][2], callback_data="02")],
        [InlineKeyboardButton(tictactoe.board[1][0], callback_data="10"),
         InlineKeyboardButton(tictactoe.board[1][1], callback_data="11"),
         InlineKeyboardButton(tictactoe.board[1][2], callback_data="12")],
        [InlineKeyboardButton(tictactoe.board[2][0], callback_data="20"),
         InlineKeyboardButton(tictactoe.board[2][1], callback_data="21"),
         InlineKeyboardButton(tictactoe.board[2][2], callback_data="22")]
    ]


async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    reply_markup = InlineKeyboardMarkup(board())
    await context.bot.send_message(chat_id=chat_id, text="let's play.", reply_markup=reply_markup)


async def button_handler(update:Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    query = update.callback_query
    data = query.data
    winner = tictactoe.checkWinner()
    if winner:
        reply_markup = InlineKeyboardMarkup(board())
        if winner == "tie":
            await query.edit_message_text(text=f"It is a tie. Send /start to play again", reply_markup=reply_markup)
            tictactoe.board_clear()
        else:
            await query.edit_message_text(text=f"The winner is {winner}. Send /start to play again", reply_markup=reply_markup)
            tictactoe.board_clear()
        return
    row = int(data[0])
    col = int(data[1])
    if tictactoe.checkOccupied(row,col):
        await context.bot.send_message(chat_id=chat_id, text="It is already occupied.")

    else:
        tictactoe.board[row][col] = 'x'
        reply_markup = InlineKeyboardMarkup(board())
        await query.edit_message_text(text="keep going!", reply_markup=reply_markup)
        winner = tictactoe.checkWinner()
        if winner:
            reply_markup = InlineKeyboardMarkup(board())
            if winner == "tie":
                await query.edit_message_text(text=f"It is a tie. Send /start to play again", reply_markup=reply_markup)
                tictactoe.board_clear()
            else:
                await query.edit_message_text(text=f"The winner is {winner}. Send /start to play again", reply_markup=reply_markup)
                tictactoe.board_clear()
            return
        tictactoe.computerMove()
        reply_markup = InlineKeyboardMarkup(board())
        await query.edit_message_text(text="keep going!", reply_markup=reply_markup)
        winner = tictactoe.checkWinner()
        if winner:
            reply_markup = InlineKeyboardMarkup(board())
            if winner == "tie":
                await query.edit_message_text(text=f"It is a tie. Send /start to play again", reply_markup=reply_markup)
                tictactoe.board_clear()
            else:
                await query.edit_message_text(text=f"The winner is {winner}. Send /start to play again", reply_markup=reply_markup)
                tictactoe.board_clear()
            return
        


if __name__ == '__main__':
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()
