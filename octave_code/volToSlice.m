function volToSlice()

#fileName = 3d .mat fileName

load dip_sim500.mat; 

m0 = min(dip_sim500(isfinite(dip_sim500(:))));
m1 = max (dip_sim500(isfinite(dip_sim500(:))))
norm_A = round(((dip_sim500 -m0)/(m1-m0)*254)+2); 

norm_A(isnan(norm_A))=1;
  
slice = zeros(size(norm_A)(1), size(norm_A)(2), 3) ;

for s = 1: size(norm_A)(3);
  
  for c = 1: size(norm_A)(1);
    for r = 1: size(norm_A)(2);
     slice(c,r, 1) = jet(256)(norm_A(c,r,s),1);
     slice(c,r, 2) = jet(256)(norm_A(c,r,s),2);
     slice(c,r, 3) = jet(256)(norm_A(c,r,s),3);
     end
  end
 imwrite(slice, strcat('output/', num2str(s) ,'.tiff'));    
end

end