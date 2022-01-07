
class Scaler:
    x_price_min = 0
    x_price_max = 0

    def __init__(self,):
        pass
        
    def inverse(self,prediction):
        upscaled = prediction * (self.x_price_max - self.x_price_min) + self.x_price_min
        return upscaled

    def fit_transform(self,seq_x):
        
        x_price_avg = Scaler.__avg(seq_x[0])
        
        for x in range(1,len(seq_x)):
            x_price_avg = (Scaler.__avg(seq_x[x])+x_price_avg)/2
            
        
        dif = x_price_avg/4
        x_price_min = x_price_avg - dif
        x_price_max = x_price_avg + dif
        self.x_price_min = x_price_min
        self.x_price_max = x_price_max

        for x in seq_x:
            x_price_scaled = (x[0,] - x_price_min) / (x_price_max - x_price_min)
            x[1,] = x_price_scaled
        
        x_volume_max=0
        for x in seq_x:
            if(x[2,] > x_volume_max):
                x_volume_max = x[2,]

        x_volume_min = x[2,]
        for x in seq_x:
            if(x[2,] < x_volume_min):
                x_volume_min = x[2,]
       
        for x in seq_x:
            x_volume_scaled = (x[2,] - x_volume_min) / (x_volume_max - x_volume_min)
            x[2,] = x_volume_scaled
            
        return seq_x[:,[1,2]]
    
    def __avg(x):
        return (x[0,]+x[1,])/2