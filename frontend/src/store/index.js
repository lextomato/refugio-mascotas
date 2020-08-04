import Vue from "vue";
import Vuex from "vuex";
import jwt_decode from 'jwt-decode';
import axios from 'axios';

Vue.use(Vuex);

// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default new Vuex.Store({
  state: {
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('token'),
    endpoints: {
      obtainJWT: 'http://localhost:8000/rest-auth/login/',
      logoutJWT: 'http://localhost:8000/rest-auth/logout/',
      refreshJWT: 'http://localhost:8000/refresh-token/',
      baseURL: 'http://localhost:8000/api/v1.0/',
    }
  },
  mutations: {
    setAuthUser(state, { authUser, isAuthenticated }) {
      Vue.set(state, 'authUser', authUser)
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    updateToken(state, newToken){
      localStorage.setItem('token', newToken);
      state.jwt = newToken;
    },
    removeToken(state){
      localStorage.removeItem('token');
      state.jwt = null;
    }
  },
  actions: {
    obtainToken(username, password){
      const payload = {
        username: username,
        password: password
      }
      axios.post(this.state.endpoints.obtainJWT, payload)
        .then((response)=>{
            this.commit('updateToken', response.data.token);
          })
        .catch((error)=>{
            console.log(error);
          })
    },
    logoutToken() {
      axios.post(this.state.endpoints.logoutJWT)
        .then((response)=>{
          this.commit('removeToken', response.data.token);
        })
        .cath((error)=>{
          console.log(error)
        })
    },
    refreshToken(){
      const payload = {
        token: this.state.jwt
      }
      axios.post(this.state.endpoints.refreshJWT, payload)
        .then((response)=>{
            this.commit('updateToken', response.data.token)
          })
        .catch((error)=>{
            console.log(error)
          })
    },
    inspectToken(){
      const token = this.state.jwt;
      if(token){
        const decoded = jwt_decode(token);
        const exp = decoded.exp
        const orig_iat = decoded.orig_iat
        if(exp - (Date.now()/1000) < 1800 && (Date.now()/1000) - orig_iat < 628200){
          this.dispatch('refreshToken')
        } else if (exp -(Date.now()/1000) < 1800){
          // DO NOTHING, DO NOT REFRESH          
        } else {
          // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        }
      }
    }
  },
  modules: {}
});
