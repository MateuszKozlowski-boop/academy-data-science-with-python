features = ['laptop_id', 'type_name', 'inches',
       'screen_resolution_width', 'screen_resolution_height', 
        'cpu', 'ram', 'memory_disk', 'memory_ssd', 'gpu', 'op_sys', 'weight']

X = laptops.loc[:, features]
y = laptops.loc[:, 'price']


# Check the shape of X and y. 

X.shape, y.shape
