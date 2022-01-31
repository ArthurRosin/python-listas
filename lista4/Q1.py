x = int(input())
h = x // 3600 #quociente da divisão dos segundo por uma hora
hr = x % 3600 #resto da divisão dos segundo por uma hora - horas
m = hr // 60 #quociente da divisão dos segundo por uma hora - minutos
s = hr % 60 #resto da divisão dos segundo por uma hora - segundos
print(f"{h:02d}:{m:02d}:{s:02d}")
 