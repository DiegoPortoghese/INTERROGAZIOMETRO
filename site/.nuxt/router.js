import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _2c9f0a6e = () => interopDefault(import('../pages/about.vue' /* webpackChunkName: "pages/about" */))
const _75081ad4 = () => interopDefault(import('../pages/chatmessages/index.vue' /* webpackChunkName: "pages/chatmessages/index" */))
const _1a5372cc = () => interopDefault(import('../pages/google-maps.vue' /* webpackChunkName: "pages/google-maps" */))
const _1356b930 = () => interopDefault(import('../pages/terms.vue' /* webpackChunkName: "pages/terms" */))
const _42142c30 = () => interopDefault(import('../pages/account/login.vue' /* webpackChunkName: "pages/account/login" */))
const _6df5df3e = () => interopDefault(import('../pages/account/password-change.vue' /* webpackChunkName: "pages/account/password-change" */))
const _b7a471a4 = () => interopDefault(import('../pages/account/password-reset.vue' /* webpackChunkName: "pages/account/password-reset" */))
const _448c69a1 = () => interopDefault(import('../pages/account/password-reset-confirm.vue' /* webpackChunkName: "pages/account/password-reset-confirm" */))
const _17603330 = () => interopDefault(import('../pages/account/profile.vue' /* webpackChunkName: "pages/account/profile" */))
const _32dd008a = () => interopDefault(import('../pages/account/registration.vue' /* webpackChunkName: "pages/account/registration" */))
const _398a86fd = () => interopDefault(import('../pages/account/registration-confirm.vue' /* webpackChunkName: "pages/account/registration-confirm" */))
const _e19c18c8 = () => interopDefault(import('../pages/account/user.vue' /* webpackChunkName: "pages/account/user" */))
const _3eb455f7 = () => interopDefault(import('../pages/account/userpreference.vue' /* webpackChunkName: "pages/account/userpreference" */))
const _9fae711e = () => interopDefault(import('../pages/classe/add/index.vue' /* webpackChunkName: "pages/classe/add/index" */))
const _0cca156c = () => interopDefault(import('../pages/classe/_id/index.vue' /* webpackChunkName: "pages/classe/_id/index" */))
const _462acad7 = () => interopDefault(import('../pages/classe/_id/gestione/index.vue' /* webpackChunkName: "pages/classe/_id/gestione/index" */))
const _3ac57ab4 = () => interopDefault(import('../pages/classe/_id/gestione/conferme.vue' /* webpackChunkName: "pages/classe/_id/gestione/conferme" */))
const _189baed3 = () => interopDefault(import('../pages/classe/_id/gestione/interrogazioni.vue' /* webpackChunkName: "pages/classe/_id/gestione/interrogazioni" */))
const _30722f7d = () => interopDefault(import('../pages/classe/_id/gestione/note.vue' /* webpackChunkName: "pages/classe/_id/gestione/note" */))
const _283dff76 = () => interopDefault(import('../pages/classe/_id/gestione/orario.vue' /* webpackChunkName: "pages/classe/_id/gestione/orario" */))
const _4c56e533 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/about",
    component: _2c9f0a6e,
    name: "about"
  }, {
    path: "/chatmessages",
    component: _75081ad4,
    name: "chatmessages"
  }, {
    path: "/google-maps",
    component: _1a5372cc,
    name: "google-maps"
  }, {
    path: "/terms",
    component: _1356b930,
    name: "terms"
  }, {
    path: "/account/login",
    component: _42142c30,
    name: "account-login"
  }, {
    path: "/account/password-change",
    component: _6df5df3e,
    name: "account-password-change"
  }, {
    path: "/account/password-reset",
    component: _b7a471a4,
    name: "account-password-reset"
  }, {
    path: "/account/password-reset-confirm",
    component: _448c69a1,
    name: "account-password-reset-confirm"
  }, {
    path: "/account/profile",
    component: _17603330,
    name: "account-profile"
  }, {
    path: "/account/registration",
    component: _32dd008a,
    name: "account-registration"
  }, {
    path: "/account/registration-confirm",
    component: _398a86fd,
    name: "account-registration-confirm"
  }, {
    path: "/account/user",
    component: _e19c18c8,
    name: "account-user"
  }, {
    path: "/account/userpreference",
    component: _3eb455f7,
    name: "account-userpreference"
  }, {
    path: "/classe/add",
    component: _9fae711e,
    name: "classe-add"
  }, {
    path: "/classe/:id?",
    component: _0cca156c,
    name: "classe-id"
  }, {
    path: "/classe/:id?/gestione",
    component: _462acad7,
    name: "classe-id-gestione"
  }, {
    path: "/classe/:id?/gestione/conferme",
    component: _3ac57ab4,
    name: "classe-id-gestione-conferme"
  }, {
    path: "/classe/:id?/gestione/interrogazioni",
    component: _189baed3,
    name: "classe-id-gestione-interrogazioni"
  }, {
    path: "/classe/:id?/gestione/note",
    component: _30722f7d,
    name: "classe-id-gestione-note"
  }, {
    path: "/classe/:id?/gestione/orario",
    component: _283dff76,
    name: "classe-id-gestione-orario"
  }, {
    path: "/",
    component: _4c56e533,
    name: "index"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
