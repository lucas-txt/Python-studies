d = float(input('Digite uma distancia em metros:'))
print('''
A medida de {}m corresponde a:
{} km
{} hm
{} dam
{:.0f} dm
{:.0f} cm
{:.0f} mm
'''.format(d, d/1000, d/100, d/10, d*10, d*100, d*1000))