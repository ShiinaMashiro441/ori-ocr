import tkinter as tk
import tkinter.font as font

# main_window
root = tk.Tk('ORI_OCR')

# components
tk.Label(root, text='Function', width=10, height=3, font=font.Font(
    size=16, weight='bold')).grid(row=0, column=0)
btn_roi = tk.Button(root, text='ROI', width=15,
                    height=3, font=font.Font(size=16, weight='bold')).grid(row=0, column=1)
btn_ocr = tk.Button(root, text='OCR', width=15,
                    height=3, font=font.Font(size=16, weight='bold')).grid(row=0, column=2)

tk.Label(root, text='-- ORI Preview Area --', font=font.Font(size=12)
         ).grid(row=1, column=0, columnspan=3)
tk.Label(root, text='-- OCR Preview Area --', font=font.Font(size=12)
         ).grid(row=3, column=0, columnspan=3)

root.mainloop()
