function output = myNormalize(data)

m0 = min(data(isfinite(data(:))));
m1 = max (data(isfinite(data(:))))
output = round(((data -m0)/(m1-m0)*254)+2); 

output(isnan(output))=1;

end