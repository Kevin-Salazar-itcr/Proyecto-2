from window import Ventana  # Asegurate de que el archivo donde está tu sistema se llame ui.py
import os
app = Ventana("Landing Page")

# ===== Header =====
header = app.addFrame(orientacion="fila", maxHeight=80)
header.addLabel("Mi Producto Increíble", jerarquia=1, fg="white")

nav = header.addInlineGroup(align="center")
for texto in ["Inicio", "Características", "Precios", "Contacto"]:
    nav.addButton(texto, lambda t=texto: print(f"Navegar a {t}"), fg="white")
nav.addButton("Salir", lambda: os._exit(0), fg="white")
# ===== Hero Section =====
hero = app.addFrame(orientacion="fila", maxHeight=200)
hero.addLabel("Descubre cómo mejorar tu negocio con nuestra solución", jerarquia=2, fg="#333333")
hero.addLabel("Una plataforma potente, simple y eficiente.", jerarquia=3, fg="#555555")

cta_group = hero.addInlineGroup(align="center")
cta_group.addButton("Comenzar Ahora", lambda: print("Ir a registro"), fg="white", font=("Helvetica", 14, "bold"))
cta_group.addButton("Ver Demo", lambda: print("Reproducir demo"), fg="black")

# ===== Características en 3 columnas =====
features = app.addFrame(orientacion="fila", maxHeight=250)

for i, feature in enumerate([
    "✅ Automatización completa\nReduce tareas repetitivas con nuestra IA integrada.",
    "📊 Panel de métricas\nMonitorea tu rendimiento en tiempo real.",
    "🔒 Seguridad avanzada\nTus datos están protegidos con cifrado de grado militar."
]):
    f = features.addFrame(orientacion="columna")
    f.addLabel(feature, jerarquia=3, justify="left", wraplength=300)

# ===== Testimonio =====
testi = app.addFrame(orientacion="fila", maxHeight=150)
testi.addLabel("“Gracias a esta plataforma, aumentamos nuestras ventas un 35% en 2 meses.”", jerarquia=3, fg="#33691e")
testi.addLabel("- Carla R., CEO de TechNova", jerarquia=4, fg="#827717")

# ===== Precios =====
pricing = app.addFrame(orientacion="fila", maxHeight=220)

plan_basic = pricing.addFrame(orientacion="columna")
plan_basic.addLabel("Plan Básico", jerarquia=2)
plan_basic.addLabel("Gratis para siempre", jerarquia=3, fg="green")
plan_basic.addLabel("✔ Usuarios limitados\n✔ Soporte básico", jerarquia=4, justify="left")
plan_basic.addButton("Elegir", lambda: print("Elegido Básico"))

plan_pro = pricing.addFrame(orientacion="columna")
plan_pro.addLabel("Plan Pro", jerarquia=2)
plan_pro.addLabel("$29 / mes", jerarquia=3, fg="#ff8f00")
plan_pro.addLabel("✔ Todo lo del Básico\n✔ Usuarios ilimitados\n✔ Análisis avanzado", jerarquia=4, justify="left")
plan_pro.addButton("Elegir", lambda: print("Elegido Pro"))

carousel = app.addFrame(orientacion="fila", maxHeight=200)
nav = carousel.addInlineGroup(align="center")
path = "C:\\Users\\ksala\\OneDrive\\Documents\\Wallpaper\\FB_IMG_1718730170192.jpg"
nav.addLabel(image_path=path, max_height=200)
nav.addLabel(image_path=path, max_height=200)
nav.addLabel(image_path=path, max_height=200)
# ===== Footer =====
footer = app.addFrame(orientacion="fila", maxHeight=120)
info = footer.addInlineGroup(align="center")
info.addLabel("© 2025 Mi Empresa", fg="white")
info.addLabel("Política de Privacidad", fg="white")
info.addLabel("Términos de Servicio", fg="white")

# Mostrar ventana
app.show()
