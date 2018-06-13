load('DIP_seis_true_58x81.mat');
m0 = min(DIP_seis_true_58x81(isfinite(DIP_seis_true_58x81(:))));
m1 = max (DIP_seis_true_58x81(isfinite(DIP_seis_true_58x81(:))));
norm_A = (DIP_seis_true_58x81 -m0)/(m1-m0 ) ;
imshow(norm_A, "colormap", jet);