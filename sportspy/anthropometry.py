class Somatotype:
    
    def endomorphy(x1,x2,x3):
        x = x1+x2+x3 # summation of all the skinfolds
        
        endo = -0.7182 + 0.1451 * x - 0.00068 * (x*x) + 0.0000014 * (x*x*x)
        
        return endo
    
    def mesomorphy(humerus_breadth,femur_breadth,corrected_arm_girth,corrected_calf_girth, height):
        
        meso = 0.858 * humerus_breadth + 0.601 * femur_breadth + 0.188 * corrected_arm_girth + 0.161 * corrected_calf_girth - height * 0.131 + 4.5
        
        return meso 
    
    def ectomorphy (height, weight):
        
        HWR = height / (weight**(1/3))
        
        if HWR >= 40.75:
            ecto = 0.732 * HWR - 28.58
            
            return ecto
        elif HWR < 40.75 and HWR > 38.25:
            
            ecto = 0.463 * HWR - 17.63
            
            return ecto
        
        else:
            
            return 0.1        
    
    