function [img, real_sizes] = tifread(fname)

    %reader = bfGetReader(fname);
    %omeMeta = reader.getMetadataStore();
    %get number of images in the folder
    a=dir([yourfolder '/*.tiff'])
    out=size(a,1)

    % image pixel, real size retrieved
    x_size_pix = omeMeta.getPixelsSizeX(0).getValue();  % image width, pixels
    y_size_pix = omeMeta.getPixelsSizeY(0).getValue();  % image height, pixels
    z_num = omeMeta.getPixelsSizeZ(0).getValue();  % # of z slices

    x_size_unit_default_value = omeMeta.getPixelsPhysicalSizeX(0).value();
    x_size_unit_default_unit = omeMeta.getPixelsPhysicalSizeX(0).unit().getSymbol();
    x_size_unit_cell = omeMeta.getPixelsPhysicalSizeX(0).value(ome.units.UNITS.MICROMETER);
    x_size_unit = x_size_unit_cell.doubleValue();

    y_size_unit_default_value = omeMeta.getPixelsPhysicalSizeY(0).value();
    y_size_unit_cell = omeMeta.getPixelsPhysicalSizeY(0).value(ome.units.UNITS.MICROMETER);
    y_size_unit = y_size_unit_cell.doubleValue();

    z_size_unit_default_value = omeMeta.getPixelsPhysicalSizeZ(0).value();
    z_size_unit_cell = omeMeta.getPixelsPhysicalSizeZ(0).value(ome.units.UNITS.MICROMETER);
    z_size_unit = z_size_unit_cell.doubleValue();

    ch_num = omeMeta.getChannelCount(0);

    % image retrieved
    img = zeros(x_size_pix, y_size_pix, z_num, ch_num, 'single');

    for i=1:z_num
        for j=1:ch_num
            img(:,:,i,j) = bfGetPlane(reader, reader.getIndex(i-1, j-1, 0)+1);
        end
    end
    
    real_sizes = [x_size_unit, y_size_unit, z_size_unit];
end