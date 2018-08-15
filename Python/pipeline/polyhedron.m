run('matlab_data.m');


alpha = 35;
blobs = 26;
shapes = {};

 for i = 1:blobs
     shapes{i} = alphaShape(x{i}',y{i}',z{i}', alpha);
 end
 
 
 for i = 1:blobs
     plot(shapes{i}, 'FaceColor', [rand(),rand(),rand()]);
     hold on;
 end


    
    
    
    