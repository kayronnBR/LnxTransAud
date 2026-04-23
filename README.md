tradutor de audio para texto instantaneo no linux (feito pelo gemini)

# como baixar?
1- baixe as dependencias:
```bash
echo "### Instalando Helvum via Flatpak ###"
flatpak install flathub org.pipewire.Helvum -y

echo "### Instalando dependências do sistema (Pacman) ###"
sudo pacman -S --needed python python-pip portaudio ffmpeg helvum base-devel wget unzip --noconfirm

echo "### Instalando bibliotecas Python no ambiente isolado ###"
pip install --upgrade pip
pip install vosk deep-translator pyaudio
```
2- baixei o aplicativo
<h1>
  <a href="https://downgit.github.io/#/home?url=https://github.com/kayronnBR/LnxTransMsg/blob/main/LnxTransMsg.sh">DOWNLOAD</a>
</h1>
extraia o arquvio

# configurando o aplicativo:
abre o arquivo `run.sh` e edite o caminho padrão `cd /home/kayronn/LnxTransAud/` para onde sua pasta do pograma esta

# iniciando aplicativo:
abre o terminal e mova o arquivo `run.sh` para o dentro do terminal e aperte ENTER para inicar o pograma

# dica:
caso queira executar o `run.sh` como aplicativo use o pins para adicionar o comando para executar

comando que eu uso:
`deepin-terminal-gtk -e bash -c "/home/kayronn/LnxTransAud/run.sh; exec bash"`
obs: precisa verifica qual seu terminal e qualquer coisa peça para IA gerar o codigo para executar
