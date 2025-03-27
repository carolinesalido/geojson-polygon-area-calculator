import geopandas as gpd
arquivo_geojson = r'.\poligono_exemplo.geojson'
arquivo_saida = r'.\poligono_exemplo_saida.geojson'
def calcula_area_poligonos(arquivo_geojson, arquivo_saida):
    try:
        gdf = gpd.read_file(arquivo_geojson)
        gdf['area_m2'] = gdf.geometry.area
        gdf.to_file(arquivo_saida, driver='GeoJSON')

        print(f'Áreas calculadas e salvas em {arquivo_saida}')
    except Exception as e:
        print(f"Erro: {e}")
calcula_area_poligonos(arquivo_geojson, arquivo_saida)