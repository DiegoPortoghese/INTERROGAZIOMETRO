import webpack from 'webpack'

export default {
  mode: 'universal',
  /*
  ** Headers of the page
  */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  //loading: { color: '#fff' },
  loading: '~/components/loading.vue',
  /*
  ** Global CSS
  */
  css: [
    '@fortawesome/fontawesome-free/css/all.css',
    '@/assets/css/main.css',
    //'@/assets/css/custom_fullcalendar.css',
    '@fullcalendar/core/main.css',
    '@fullcalendar/daygrid/main.css',
  ],
  
  script: [
    { src: 'https://code.jquery.com/jquery-3.4.1.min.js' }
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    { src: '~/plugins/full-calendar', ssr: false },
    { src: '~/plugins/jquery', ssr: false },
  ],

  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://bootstrap-vue.js.org
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    '@nuxtjs/font-awesome',
    'bootstrap-vue/nuxt',
    'cookie-universal-nuxt',
  ],
  axios: {
    baseURL: 'http://localhost:8000/',
  },
  auth: {
    redirect: {
      login: '/account/login/',
      logout: '/',
      home: '/'
    },
    strategies: {
      local: {
        endpoints: {
          login: { url: 'rest-auth/login/', method: 'post', propertyName: 'key'},
          user: { url: 'rest-auth/user/', method: 'get', propertyName: false },
          logout: { url: 'rest-auth/logout/', method: 'post'}
        },
        tokenName: 'Authorization',
        tokenType: 'Token'
      }
    }
  },
  /*
  ** Build configuration
  */
  build: {
    plugins: [
        new webpack.ProvidePlugin({  
          jQuery: 'jquery',
          $: 'jquery',
          'window.jQuery': 'jquery',
        }),

    ]
  }


  /*{ src: "~/plugins/google-maps", ssr: true }*/
 /*
  build: {
    extend (config, ctx) {
    },
    transpile: [/^vue2-google-maps($|\/)/]
  }*/

}
