from textwrap import fill
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
#from qrcode.image.styles.colormasks import RadialGradiantColorMask

# Solicitar informações do usuário
nomerede = input("Digite o nome da rede: ")
senhaRede = input("Digite a senha da rede: ")
nomeFinal = input("Digite o nome do arquivo: ")

# Informações do Wi-Fi
ssid = nomerede
password = senhaRede
security = "WEP"  # Pode ser 'WPA', 'WEP' ou deixar vazio para redes abertas

# Formato do texto para o QR Code
wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"

# Gerar o QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    
)
qr.add_data(wifi_config)
qr.make(fit=True)

# Criar a imagem do QR Code
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    #color_mask=RadialGradiantColorMask(),
    embeded_image_path="logoFamilia_FB.png",
    fill_color="blue",
    back_color="gray",
)

# Salvar a imagem
img.save(f"{nomeFinal}.png")

print("QR Code gerado e salvo!")