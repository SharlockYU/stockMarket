
import { createApp } from 'vue'
import 'babel-polyfill'
import App from './App.vue'

//import Vue from 'vue'
import Es6Promise from 'es6-promise'
Es6Promise.polyfill()
createApp(App).mount('#app')
