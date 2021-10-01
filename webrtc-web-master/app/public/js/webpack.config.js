const path = require('path');
    module.exports = {
      entry: '../ind',
      output: {
        path: path.resolve('./'),
        filename: 'webpack.bundle.js'
      },
      resolve: {
        alias: {
          'node_modules': path.join('../', 'node_modules'),
        }
      }
    };