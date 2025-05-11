from window import Ventana  # Asegurate de que el archivo donde está tu sistema se llame ui.py

app = Ventana("Landing Page")

# ===== Header =====
header = app.addFrame(fila=True, minheight=80, color="#283593")
header.addLabel("Mi Producto Increíble", jerarquia=1, fg="white", bg="#283593")

nav = header.addInlineGroup(align="center")
for texto in ["Inicio", "Características", "Precios", "Contacto"]:
    nav.addButton(texto, lambda t=texto: print(f"Navegar a {t}"), bg="#5c6bc0", fg="white")

# ===== Hero Section =====
hero = app.addFrame(fila=True, minheight=200, color="#f5f5f5")
hero.addLabel("Descubre cómo mejorar tu negocio con nuestra solución", jerarquia=2, fg="#333333", bg="#f5f5f5")
hero.addLabel("Una plataforma potente, simple y eficiente.", jerarquia=3, fg="#555555", bg="#f5f5f5")

cta_group = hero.addInlineGroup(align="center")
cta_group.addButton("Comenzar Ahora", lambda: print("Ir a registro"), bg="#43a047", fg="white", font=("Helvetica", 14, "bold"))
cta_group.addButton("Ver Demo", lambda: print("Reproducir demo"), bg="#eeeeee", fg="black")

# ===== Características en 3 columnas =====
features = app.addFrame(fila=True, minheight=250, color="#ffffff")

for i, feature in enumerate([
    "✅ Automatización completa\nReduce tareas repetitivas con nuestra IA integrada.",
    "📊 Panel de métricas\nMonitorea tu rendimiento en tiempo real.",
    "🔒 Seguridad avanzada\nTus datos están protegidos con cifrado de grado militar."
]):
    f = features.addFrame(columna=True, color="#e8eaf6")
    f.addLabel(feature, jerarquia=3, justify="left", wraplength=300)

# ===== Testimonio =====
testi = app.addFrame(fila=True, minheight=150, color="#f1f8e9")
testi.addLabel("“Gracias a esta plataforma, aumentamos nuestras ventas un 35% en 2 meses.”", jerarquia=3, fg="#33691e")
testi.addLabel("- Carla R., CEO de TechNova", jerarquia=4, fg="#827717")

# ===== Precios =====
pricing = app.addFrame(fila=True, minheight=220, color="#ffffff")

plan_basic = pricing.addFrame(columna=True, color="#fafafa")
plan_basic.addLabel("Plan Básico", jerarquia=2)
plan_basic.addLabel("Gratis para siempre", jerarquia=3, fg="green")
plan_basic.addLabel("✔ Usuarios limitados\n✔ Soporte básico", jerarquia=4, justify="left")
plan_basic.addButton("Elegir", lambda: print("Elegido Básico"), bg="#c8e6c9")

plan_pro = pricing.addFrame(columna=True, color="#fff9c4")
plan_pro.addLabel("Plan Pro", jerarquia=2)
plan_pro.addLabel("$29 / mes", jerarquia=3, fg="#ff8f00")
plan_pro.addLabel("✔ Todo lo del Básico\n✔ Usuarios ilimitados\n✔ Análisis avanzado", jerarquia=4, justify="left")
plan_pro.addButton("Elegir", lambda: print("Elegido Pro"), bg="#ffe082")

# ===== Footer =====
footer = app.addFrame(fila=True, minheight=120, color="#263238")
info = footer.addInlineGroup(align="center")
info.addLabel("© 2025 Mi Empresa", fg="white", bg="#263238")
info.addLabel("Política de Privacidad", fg="white", bg="#263238")
info.addLabel("Términos de Servicio", fg="white", bg="#263238")

# Mostrar ventana
app.show()
