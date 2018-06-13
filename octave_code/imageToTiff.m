function imageToTiff()

load DIP_seis_obs_234x326.mat; 

norm_A = myNormalize(DIP_seis_obs_234x326);
  
image = zeros(size(norm_A)(1), size(norm_A)(2), 3) ;

size(image)

for c = 1: size(image)(1);
    for r = 1: size(image)(2);
     image(c,r, 1) = jet(256)(norm_A(c,r),1);
     image(c,r, 2) = jet(256)(norm_A(c,r),2);
     image(c,r, 3) = jet(256)(norm_A(c,r),3);
     end
  end
 imwrite(image, strcat('output2/', 'DIP_seis_obs_234x326' ,'.tiff'));    



end