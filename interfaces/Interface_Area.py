import folium
import tkinter as tk
from tkinter import filedialog
import webbrowser
import os

class Area:
    def __init__(self, area_id: int, name:str , location: str, size: int, company_id: int) -> None:
        self.area_id = area_id
        self.name = name
        self.location = location
        self.size = size
        self.company_id = company_id
    
    def escolher_diretorio(self) -> str:
        """
        Abre uma janela para o usuário escolher um diretório.
        """
        root = tk.Tk()
        root.withdraw()  # Ocultar a janela principal do Tkinter
        script_dir = os.path.dirname(os.path.abspath(__file__))
        diretorio = filedialog.askdirectory(initialdir=script_dir)
        return diretorio
    
    def exibir_Area(self) -> None:
        """
        @brief Função que exibe as informações da área e abre um mapa com a localização da área junto de um marcador para delimintar a área.
        """
        try:
            print(f"Nome: {self.name}")
            latitude, longitude = self.location.split('_')
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            print(f"Raio (m2): {self.size}")

            latitude = float(latitude)
            longitude = float(longitude)
            size = int(self.size)

            m = folium.Map(location=[latitude, longitude], zoom_start=2)
            folium.Circle(
                location=[latitude, longitude],
                radius=size,
                color='crimson',
                weight=1,
                fill_opacity=0.5,
                opacity=1,
                fill_color='crimson',
                popup=f"{self.name} - Raio: {size} m2",
                tooltip="Clique para ver mais informações!",
            ).add_to(m)

            # Escolher o diretório para salvar o mapa
            diretorio = self.escolher_diretorio()
            nome_arquivo = f'{self.name}_mapa.html'
            if diretorio:
                file_path = os.path.join(diretorio, nome_arquivo)
                m.save(file_path)
                # Abrir o arquivo HTML no navegador padrão
                webbrowser.open('file://' + file_path)
                print(f"Mapa salvo em: {file_path}")
            else:
                print("Nenhum diretório selecionado. O mapa não foi salvo.")

        except Exception as e:
            print(f"Erro ao exibir a área: {e}")


