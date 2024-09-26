import math

def euclideanDistance(point1,point2):
    return math.sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)
    

points=[(1,2),(4,6),(5,7),(3,1),(7,3)]


distances=[]



for i in range(len(points)):
    for j in range(len(points)):
        distance =euclideanDistance(points[i],points[j])
        distances.append(distance)
        
        
        
# Minimum mesafeyi bul
min_distance = min(distances)

# Sonuçları yazdır
print("Tüm noktalar arasındaki mesafeler:", distances)
print("En küçük mesafe:", min_distance)