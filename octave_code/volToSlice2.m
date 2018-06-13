function volToSlice2()

#fileName = 3d .mat fileName

load images_border_fade_234x326.mat; 

m0 = min(images_border_fade_234x326(isfinite(images_border_fade_234x326(:))));
m1 = max (images_border_fade_234x326(isfinite(images_border_fade_234x326(:))))
norm_A = round(((images_border_fade_234x326 -m0)/(m1-m0)*254)+2); 

norm_A(isnan(norm_A))=1;
  
slice = zeros(size(norm_A)(2), size(norm_A)(3), 3) ;

for s = 1: size(norm_A)(1);
  
  for c = 1: size(norm_A)(2);
    for r = 1: size(norm_A)(3);
     slice(c,r, 1) = jet(256)(norm_A(s,c,r),1);
     slice(c,r, 2) = jet(256)(norm_A(s,c,r),2);
     slice(c,r, 3) = jet(256)(norm_A(s,c,r),3);
     end
  end
 imwrite(slice, strcat('output/', num2str(s) ,'.tiff'));    
end

end