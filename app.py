
import cv2

def capturar_e_salvar():
    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
        print("Erro ao abrir a webcam.")
        return

    print("[1] Efeito JET")
    print("[2] Efeito INFERNO")
    print("[3] Efeito PLASMA")
    print("[ESPAÇO] Salvar foto")
    print("[ESC] Sair")

    efeito = cv2.COLORMAP_JET

    while True:
        status, frame = webcam.read()

        if not status:
            print("Falha ao receber o frame da webcam.")
            break

        foto_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        foto_termica = cv2.applyColorMap(foto_cinza, efeito)

        cv2.imshow("Camera com efeito termico", foto_termica)

        tecla = cv2.waitKey(1) & 0xFF

        if tecla == ord('1'):
            efeito = cv2.COLORMAP_JET
            print("Efeito JET selecionado")

        elif tecla == ord('2'):
            efeito = cv2.COLORMAP_INFERNO
            print("Efeito INFERNO selecionado")

        elif tecla == ord('3'):
            efeito = cv2.COLORMAP_PLASMA#
            print("Efeito PLASMA selecionado")

        elif tecla == 32:
            cv2.imwrite("foto_termica.jpeg", foto_termica)
            print("Foto térmica salva: foto_termica.jpeg")

        elif tecla == 27:
            print("Encerrando câmera...")
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capturar_e_salvar()
