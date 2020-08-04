<template lang="html">
  <div class="container text-center">
    <h1 class="my-4">Inicio de sesión</h1>
    <hr width="55%" />

    <b-form class="mb-3">
      <b-form-group
        id="input-group-username"
        label="Username:"
        label-for="input-username"
      >
        <b-form-input
          class="wmax-20 mx-auto"
          id="input-username"
          v-model="username"
          required
          autofocus="autofocus"
          type="text"
          placeholder="Ingrese su Username"
        ></b-form-input>
      </b-form-group>
    </b-form>

    <b-form class="mb-3">
      <b-form-group
        id="input-group-contraseña"
        label="Contraseña:"
        label-for="input-contraseña"
      >
        <b-form-input
          class="wmax-20 mx-auto"
          id="input-contraseña"
          v-model="password"
          required
          autofocus="autofocus"
          type="password"
          placeholder="Ingrese su contraseña"
        ></b-form-input>
      </b-form-group>
      <button
        @click.prevent="authenticate"
        class="btn btn-primary"
        type="submit">
        Iniciar sesión
      </button>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    authenticate () {
      const payload = {
        username: this.username,
        password: this.password
      }
      axios.post(this.$store.state.endpoints.obtainJWT, payload)
        .then((response) => {
          this.$store.commit('updateToken', response.data.token)
          // get and set auth user
          const base = {
            baseURL: this.$store.state.endpoints.baseUrl,
            headers: {
            // Set your Authorization to 'JWT', not Bearer!!!
              Authorization: `JWT ${this.$store.state.jwt}`,
              'Content-Type': 'application/json'
            },
            xhrFields: {
                withCredentials: true
            }
          }
          // Even though the authentication returned a user object that can be
          // decoded, we fetch it again. This way we aren't super dependant on
          // JWT and can plug in something else.
          const axiosInstance = axios.create(base)
          axiosInstance({
            url: "/rest-auth/user/",
            method: "get",
            params: {}
          })
            .then((response) => {
              this.$store.commit("setAuthUser",
                {authUser: response.data, isAuthenticated: true}
              )
              this.$swal.fire(
                'Inició sesión exitosamente!',
                'Presiona ok!',
                'success'
              )
              this.$router.push({name: 'Home'})
            })

        })
        .catch((error) => {
          this.$swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Credenciales incorrectas',
          })
          console.log(error);
          console.debug(error);
          console.dir(error);
        })
    }
  }
}
</script>

<style scoped>
  .wmax-20 {
    max-width: 20rem!important;
  }
</style>