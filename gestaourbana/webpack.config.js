const MinifyPlugin = require("babel-minify-webpack-plugin");
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');

module.exports = {
	entry: "./static/js/src/index.js",
	output: {
		filename: "./static/js/bundle.min.js"
	},
	module: {
		loaders: [
			{
				test: /\.js$/,
				loader: 'babel-loader',
				exclude:  /(node_modules|bower_components)/,
				query: {
					presets: ['es2015']
				}
			},
			{
				test: /\.scss$/,
				loader: ExtractTextPlugin.extract('css-loader!sass-loader')
			}
		]
	},
	plugins: [
		new MinifyPlugin(),
		new ExtractTextPlugin('static/css/style.min.css', {
			allChunks: true
		}),
		new OptimizeCssAssetsPlugin({
			cssProcessorOptions: { discardComments: { removeAll: true } }
		})
	 ]
}