import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class WidgetManager:
    def __init__(self):
        self.widgets = {}

    def register(self, widget_id, widget):
        if widget_id:
            self.widgets[widget_id] = widget

    def get(self, widget_id):
        return self.widgets.get(widget_id, None)

class InlineGroup:
    def __init__(self, frame, manager, align="left"):
        self.frame = frame
        self.widget_manager = manager
        self.imagenes = []

        if align == "center":
            self.frame.pack(anchor="center", fill="x")
        elif align == "right":
            self.frame.pack(anchor="e", fill="x")
        else:
            self.frame.pack(anchor="w", fill="x")

    def addButton(self, text, command, id=None, **kwargs):
        kwargs.setdefault("bg", self.frame["bg"])
        btn = tk.Button(self.frame, text=text, command=command, **kwargs)
        expand = "width" not in kwargs
        btn.pack(side="left", padx=5, expand=expand, fill="both" if expand else None)
        self.widget_manager.register(id, btn)
        return btn

    def addLabel(self, text=None, image_path=None, max_height=None, jerarquia=4, id=None, **kwargs):
        kwargs.setdefault("bg", self.frame["bg"])
        if image_path:
            img = Image.open(image_path)
            if max_height:
                ratio = max_height / img.height
                new_width = int(img.width * ratio)
                img = img.resize((new_width, max_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(self.frame, image=photo, **kwargs)
            label.image = photo
            self.imagenes.append(photo)
        else:
            size = {1: 24, 2: 18, 3: 14, 4: 12}.get(jerarquia, 12)
            kwargs.setdefault("font", ("Helvetica", size))
            label = tk.Label(self.frame, text=text, **kwargs)

        expand = "width" not in kwargs
        label.pack(side="left", padx=5, expand=expand, fill="both" if expand else None)
        self.widget_manager.register(id, label)
        return label

class ContenedorFlexible:
    def __init__(self, master, orientacion='fila', maxHeight=0, bg="#ffffff", use_grid=False, manager=None, bordered=True):
        self.frame = tk.Frame(master, bd=2 if bordered else 0, relief="solid" if bordered else "flat", bg=bg)
        self.orientacion = orientacion
        self.use_grid = use_grid
        self.hijos = []
        self.imagenes = []
        self.widget_manager = manager or WidgetManager()
        self.grid_row = 0
        self.grid_col = 0

        if not use_grid:
            self.frame.pack(side='left' if orientacion == "columna" else None, fill='both', expand=True, pady=4, padx=4)
            if maxHeight > 0:
                self.frame.config(height=maxHeight)
                self.frame.pack_propagate(False)

    def addFrame(self, orientacion="fila", maxHeight=0, bg="#ffffff", use_grid=False, bordered=True):
        nuevo = ContenedorFlexible(self.frame, orientacion, maxHeight, bg, use_grid, manager=self.widget_manager, bordered=bordered)
        self.hijos.append(nuevo)
        return nuevo

    def addInlineGroup(self, align="left"):
        group = tk.Frame(self.frame, bg=self.frame["bg"])
        return InlineGroup(group, self.widget_manager, align=align)

    def _place_widget(self, widget):
        if self.use_grid:
            widget.grid(row=self.grid_row, column=self.grid_col, padx=5, pady=3, sticky="w")
            self.grid_col += 1
        else:
            widget.pack(pady=3)

    def addLabel(self, text=None, image_path=None, width=None, height=None, jerarquia=None, bg=None, id=None, **kwargs):
        kwargs.setdefault("bg", bg or self.frame["bg"])
        if image_path:
            img = Image.open(image_path)
            if width and height:
                img = img.resize((width, height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(self.frame, image=photo, **kwargs)
            label.image = photo
            self.imagenes.append(photo)
        else:
            size = {1: 24, 2: 18, 3: 14, 4: 12}.get(jerarquia, 12)
            kwargs.setdefault("font", ("Helvetica", size))
            label = tk.Label(self.frame, text=text, **kwargs)

        self._place_widget(label)
        self.widget_manager.register(id, label)
        return label

    def addInput(self, width=30, id=None, **kwargs):
        kwargs.setdefault("bg", self.frame["bg"])
        entry = tk.Entry(self.frame, width=width, **kwargs)
        self._place_widget(entry)
        self.widget_manager.register(id, entry)
        return entry

    def addText(self, width=30, height=5, id=None, **kwargs):
        kwargs.setdefault("bg", self.frame["bg"])
        txt = tk.Text(self.frame, width=width, height=height, **kwargs)
        self._place_widget(txt)
        self.widget_manager.register(id, txt)
        return txt

    def addCombobox(self, values, width=30, id=None, **kwargs):
        kwargs.setdefault("background", self.frame["bg"])
        combo = ttk.Combobox(self.frame, values=values, width=width, **kwargs)
        self._place_widget(combo)
        self.widget_manager.register(id, combo)
        return combo

    def addListbox(self, items, height=5, id=None, **kwargs):
        kwargs.setdefault("bg", self.frame["bg"])
        listbox = tk.Listbox(self.frame, height=height, **kwargs)
        for item in items:
            listbox.insert(tk.END, item)
        self._place_widget(listbox)
        self.widget_manager.register(id, listbox)
        return listbox

    def addCheckbutton(self, text, id=None, **kwargs):
        kwargs.setdefault("bg", self.frame["bg"])
        var = tk.BooleanVar()
        chk = tk.Checkbutton(self.frame, text=text, variable=var, **kwargs)
        self._place_widget(chk)
        self.widget_manager.register(id, var)
        return var

    def addRadiobutton(self, text, variable, value, **kwargs):
        kwargs.setdefault("bg", self.frame["bg"])
        rbtn = tk.Radiobutton(self.frame, text=text, variable=variable, value=value, **kwargs)
        self._place_widget(rbtn)
        return rbtn

    def addScale(self, from_=0, to=100, orient=tk.HORIZONTAL, id=None, **kwargs):
        kwargs.setdefault("bg", self.frame["bg"])
        scale = tk.Scale(self.frame, from_=from_, to=to, orient=orient, **kwargs)
        self._place_widget(scale)
        self.widget_manager.register(id, scale)
        return scale

    def addSpinbox(self, from_=0, to=10, width=5, id=None, **kwargs):
        kwargs.setdefault("bg", self.frame["bg"])
        spin = tk.Spinbox(self.frame, from_=from_, to=to, width=width, **kwargs)
        self._place_widget(spin)
        self.widget_manager.register(id, spin)
        return spin

    def addButton(self, text, command, id=None, **kwargs):
        kwargs.setdefault("bg", self.frame["bg"])
        btn = tk.Button(self.frame, text=text, command=command, **kwargs)
        self._place_widget(btn)
        self.widget_manager.register(id, btn)
        return btn

    def get(self, widget_id):
        return self.widget_manager.get(widget_id)

class Ventana:
    def __init__(self, titulo="Ventana", root=None):
        self.is_main = root is None
        self.window = tk.Tk() if self.is_main else tk.Toplevel(root)
        self.window.title(titulo)
        self.window.state('zoomed')

        self.window.protocol("WM_DELETE_WINDOW", self.cerrar)

        self.canvas = tk.Canvas(self.window, bg="#ffffff")
        self.scroll_y = tk.Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
        self.root_frame = tk.Frame(self.canvas, bg="#ffffff")
        self.canvas_window_id = self.canvas.create_window((0, 0), window=self.root_frame, anchor="nw")

        self.root_frame.bind("<Configure>", self._expand_root_frame)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_window_id, width=e.width))

        self.canvas.configure(yscrollcommand=self.scroll_y.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scroll_y.pack(side="right", fill="y")

        self.widget_manager = WidgetManager()
        self.raiz = ContenedorFlexible(self.root_frame, orientacion='fila', bg="#ffffff", manager=self.widget_manager)

    def _expand_root_frame(self, event):
        self.canvas.itemconfig(self.canvas_window_id, width=self.canvas.winfo_width())
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.canvas.update_idletasks()
        if self.canvas.bbox("all")[3] < self.canvas.winfo_height():
            self.canvas.itemconfig(self.canvas_window_id, height=self.canvas.winfo_height())

    def _on_mousewheel(self, event):
        direction = -1 if event.delta > 0 or event.num == 4 else 1
        self.canvas.yview_scroll(direction, "units")

    def cerrar(self):
        self.window.destroy()

    def show(self):
        if self.is_main:
            self.window.mainloop()
        else:
            self.window.deiconify()

    def hide(self):
        self.window.withdraw()

    def addFrame(self, orientacion="fila", maxHeight=0, color="#ffffff", use_grid=False, bordered=False):
        return self.raiz.addFrame(orientacion, maxHeight=maxHeight, bg=color, use_grid=use_grid, bordered=bordered)

    def get(self, widget_id):
        return self.widget_manager.get(widget_id)
