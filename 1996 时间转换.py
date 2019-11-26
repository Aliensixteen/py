#http://acm.zzuli.edu.cn/problem.php?id=1996&csrf=jvrZrTaJUgCluGZJqWZU93OZhAJX4wCx
t = int(input())
a = t / 3600
b = t % 3600 /60
c = t % 3600 % 60
print('%d:%d:%d'%(a,b,c)) 