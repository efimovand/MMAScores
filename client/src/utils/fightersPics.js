// Dynamically import all images from the pic_fighters folder
const fighterImages = require.context('../pic_fighters', false, /\.png$/);

// Create an object mapping image names to image imports
const fightersPics = fighterImages.keys().reduce((acc, file) => {
  const name = file.replace('./', '').replace('.png', ''); // Extract image name
  acc[`${name}_img`] = fighterImages(file); // Add image to object
  return acc;
}, {});


export default fightersPics;
