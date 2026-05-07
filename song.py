import time

colores = [
    '\033[96m', # Cian claro
    '\033[94m', # Azul claro
    '\033[92m', # Verde claro
    '\033[36m', # Cian oscuro
]
RESET = '\033[0m'

# Lista completa de Scandic
letras = [
    ("Ey, uh", 0.08, "🎤"),
    ("Pa' toa' las pibas, quiero verla' con la copa arriba", 0.05, "🥂"),
    ("Bailando hasta abajo, se moti–", 0.05, "💃"),
    ("", 0.1, ""), # Pausa
    ("Tú tienes todo eso que me encanta", 0.06, "✨"),
    ("Y yo quiero ver hasta dónde es que aguanta'", 0.05, "👀"),
    ("Me tiene mal esa carita de santa", 0.06, "😇"),
    ("Pero sé que eres mala, baby", 0.06, "😈"),
    ("", 0.1, ""),
    ("(Uh-uh, yeah) tienes to' eso, mami", 0.06, "🔥"),
    ("(Uh-uh, hum, yeah) to' eso que me pone malo", 0.06, "🥵"),
    ("(Uh-uh, ja, ja) si lo pides, me caso", 0.05, "💍"),
    ("(Uh-uh, uh) nah, en verdad, no me hagas caso", 0.05, "😅"),
    ("", 0.1, ""),
    ("Hazme el favor, que", 0.07, "🙏"),
    ("Si hay algo que yo no sé dar es dar amor", 0.05, "🖤"),
    ("Y sé que soy malo, sé que soy lo peor", 0.05, "🌩️"),
    ("No soy pa' ti, yo te lo había advertido", 0.05, "⚠️"),
    ("Mientras más corto, más divertido", 0.05, "⏱️"),
    ("", 0.1, ""),
    ("Pero mala, baby, no seas mala, baby, no seas mala", 0.04, "🥀"),
    ("(Yo voy a ser to' lo mala que tú quiera')", 0.05, "🤫"),
    ("Mala, entonces séme mala, entonces séme mala", 0.04, "🖤"),
    ("(Cállate y no alargue' más la espera)", 0.05, "⏳"),
    ("", 0.1, ""),
    ("(Shh) y yo calla'íto", 0.06, "🤐"),
    ("Bajando poco a poquito", 0.06, "📉"),
    ("Vamo' a perrear lento, no te me quito", 0.05, "🎶"),
    ("Mi felina, Héctor y Tito", 0.06, "🐈‍⬛"),
    ("", 0.1, ""),
    ("Player desde la Scandic, lleva tiempo ya", 0.05, "🏨"),
    ("En la calle, la tienes controlá'", 0.05, "🌃"),
    ("Si me lo pides, baby, yo me porto mal", 0.05, "😈"),
    ("Tú eres mala, déjame comprobar", 0.06, "🔍"),
    ("", 0.1, ""),
    ("Hum, yo no soy bonito ni na' de eso", 0.06, "🤷‍♂️"),
    ("Pero como Yomo, te la dejo caer con to' el peso", 0.04, "⚓"),
    ("Menos mal que no se escucha lo que pienso", 0.05, "🧠"),
    ("A mí tú me suenas de algo, y creo que de Los Brezos, mami", 0.04, "📍"),
    ("", 0.1, ""),
    ("Ja, me dejaron roto y tú me lo puedes curar con un besito", 0.04, "🩹"),
    ("Nah, juro no volver a hablarte de eso, mi amor", 0.05, "🤐"),
    ("", 0.1, ""),
    ("(Uh-uh, yeah) tienes to' eso, mami", 0.06, "🔥"),
    ("(Uh-uh, hum, yeah) to' eso que me pone malo", 0.06, "🥵"),
    ("(Uh-uh, ja, ja) si lo pides, me caso", 0.05, "💍"),
    ("(Uh-uh, uh) nah, en verdad, no me hagas caso", 0.05, "😅"),
    ("", 0.1, ""),
    ("Hazme el favor, que", 0.07, "🙏"),
    ("Si hay algo que yo no sé dar es dar amor", 0.05, "🖤"),
    ("Y sé que soy malo, sé que soy lo peor", 0.05, "🌩️"),
    ("No soy pa' ti, yo te lo había advertido", 0.05, "⚠️"),
    ("Mientras más corto, más divertido", 0.05, "⏱️"),
    ("", 0.1, ""),
    ("Pero mala, baby, no seas mala, baby, no seas mala", 0.04, "🥀"),
    ("(Yo voy a ser to' lo mala que tú quiera')", 0.05, "🤫"),
    ("Mala, entonces séme mala, entonces séme mala", 0.04, "🖤"),
    ("(Cállate y no alargue' más la espera)", 0.05, "⏳"),
    ("", 0.1, ""),
    ("Es mejor si no me complico", 0.06, "🧊"),
    ("Hagamos como que ninguno tiene el alma rota (tiene el alma rota)", 0.05, "💔"),
    ("Es mejor así, calla'íto", 0.06, "🤫"),
    ("Haciendo como que ninguno se equivoca", 0.05, "🎭"),
    ("", 0.1, ""),
    ("Solamente soy un perro sato", 0.06, "🐕"),
    ("Pidiendo cariño na' más por un rato (solo por un rato, mi amor)", 0.05, "🥺"),
    ("Sé que tú también eres lo mismo", 0.06, "🪞"),
    ("Dos diablitos comiendo del mismo plato", 0.05, "🍽️"),
    ("", 0.1, ""),
    ("Hagamos como que ninguno tiene el alma rota", 0.05, "💔"),
    ("(Hagamos como–, hagamos como–, tiene el alma rota)", 0.04, "🌧️"),
    ("(Hagamos como–, hagamos como–, tiene el alma rota)", 0.04, "🌧️"),
    ("(Hagamos como–, hagamos como–, tiene el alma rota)", 0.04, "🌧️"),
    ("", 0.1, ""),
    ("Claro, claro, claro que tiene' el alma rota", 0.05, "🥀"),
    ("Niña buena, no me escupiría' en la boca", 0.05, "💧"),
    ("Tú solo me buscas cuando estás en nota", 0.05, "🥂"),
    ("Tú estás buena, pero estás loca", 0.06, "🌪️"),
    ("", 0.1, ""),
    ("Baby, tú me mandas selfies en la cama en el amanecer (en el amanecer)", 0.04, "🌅"),
    ("Y cuando estoy bebiendo, el diablito del hombro no tarda en aparecer", 0.04, "🥃"),
    ("Y esa eres tú", 0.08, "👉"),
]

def mostrar_letras():
    for i, (linea, velocidad, emoji) in enumerate(letras):
        # Si la línea está vacía, es solo una pausa, no imprimimos nada
        if not linea:
            print()
            time.sleep(0.5)
            continue
            
        color = colores[i % len(colores)]
        print(color, end="") 
        
        for caracter in linea:
            print(caracter, end="", flush=True)
            time.sleep(velocidad) 
            
        print(f" {emoji}{RESET}")
        time.sleep(0.6) # Tiempo de espera general entre barras

if __name__ == "__main__":
    mostrar_letras()