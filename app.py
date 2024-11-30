import streamlit as st
import speech_recognition as sr

# Configuración de la aplicación
st.title("🎙️ Transcriptor de Voz a Texto")
st.write("Habla en tu micrófono y ve cómo tus palabras se transcriben en tiempo real.")

# Botón para iniciar la transcripción
start_button = st.button("🎤 Iniciar Transcripción")

# Texto donde aparecerán los resultados
transcription = st.empty()

# Función para capturar y transcribir el audio
def transcribe_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Escuchando... Habla ahora")
        try:
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio_data, language="es-ES")
            return text
        except sr.WaitTimeoutError:
            return "⏳ No se detectó voz a tiempo. Inténtalo de nuevo."
        except sr.UnknownValueError:
            return "🤔 No pude entender lo que dijiste. Por favor, inténtalo otra vez."
        except sr.RequestError as e:
            return f"⚠️ Error del servicio: {e}"

# Accionar la transcripción al hacer clic
if start_button:
    result = transcribe_audio()
    transcription.write(f"**Transcripción:** {result}")
