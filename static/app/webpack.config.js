var path = require('path');
var webpack = require('webpack');


module.exports = {
	entry: {
		app: './js/main.js',
		vendor: ['angular', 'angular-ui-router', 'angular-local-storage', 'angular-ui-bootstrap']
	},
	output: {
		path: path.resolve(__dirname, 'build'),
		filename: 'main.bundle.js'
	},
	plugins: [
    	new webpack.optimize.CommonsChunkPlugin({name: "vendor", filename:"vendor.bundle.js"})
	],
	module: {
		loaders: [
			{
				test: /\.js$/,
				loader: 'babel-loader',
				query: {
					presets: ['es2015']
				}
			}
		]
	},
	stats: {
		colors: true
	},
	watch: true
}
