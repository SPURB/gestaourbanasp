const MinifyPlugin = require("babel-minify-webpack-plugin");
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const Webpack = require("webpack");

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
			},
			{ 
				test: /\.(ttf|eot|svg|woff(2)?)(\?[a-z0-9=&.]+)?$/,
				loader: 'file-loader',
				options: {
					outputPath: 'static/css/fonts/',
					publicPath: '../../'
				}
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
		}),
		new Webpack.ProvidePlugin({
            $: "jquery",
            jquery: "jquery",
            jQuery: "jquery"
        })
	 ]
}