<template>
  <div>
    <div>
      <b-navbar
        style="transition-duration: .5s"
        fixed="top"
        class="shadow-lg"
        toggleable="lg"
        type="light"
        :class="{ 'bg-light': sCroll }"
        variant="faded"
        @scroll="handleSCroll"
      >
        <b-navbar-brand to="/"
          ><b-icon icon="house" aria-hidden="true"></b-icon>
          Home</b-navbar-brand
        >

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item to="/nosotros">Nosotros</b-nav-item>
            <b-nav-item to="/mascotas">Mascotas</b-nav-item>
            <b-nav-item to="/mascotas/solicitud">Solicitud</b-nav-item>
            <b-nav-item to="/noticias-comunidad">Noticias</b-nav-item>
            <b-nav-item href="#contacto">Contacto</b-nav-item>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template v-slot:button-content>
                <b-icon icon="gear" aria-hidden="true"></b-icon>
              </template>
              <b-dropdown-item class="text-center" disabled>Uso Interno</b-dropdown-item>
              <b-dropdown-item v-if="!$store.state.jwt" to="/login"><b-icon variant="dark" icon="person-plus-fill"></b-icon> Iniciar sesión</b-dropdown-item>
              <b-dropdown-item v-if="$store.state.jwt" to="/dashboard"><b-icon variant="dark" icon="app-indicator"></b-icon> Dashboard Admin</b-dropdown-item>
              <b-dropdown-item v-if="$store.state.jwt" @click.prevent="logoutSession"><b-icon variant="dark" icon="person-dash-fill"></b-icon> Cerrar sesión</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>

    <div id="app" class="page-content">
      <!-- Button Scroll 0 -->
      <div
        @click="scrollToTop"
        :class="[showBt ? 'animate__bounceInUp' : 'animate__bounceOutDown']"
        style="position: fixed!important; bottom:.05rem!important; right: 1rem!important;"
        class="animate__animated btn btn-info rounded-circle mb-5 ir-arriba"
      >
        <b-icon font-scale="2.5" icon="chevron-up"></b-icon>
      </div>
      <!-- /.Button -->
      <transition name="slide" mode="out-in" appear>
        <router-view />
      </transition>
    </div>

    <footer id="sticky-footer" class="mt-3 py-4 bg-dark text-white-50">
      <div class="mt-3 container mx-auto text-center">
        <div class="row">
          <div class="col-md-6 col-sm-12 mx-auto text-center">
            <svg class="expand mx-1" width="48" height="48" viewBox="0 0 48 48">
              <path
                d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-3 7h-1.924c-.615 0-1.076.252-1.076.889v1.111h3l-.238 3h-2.762v8h-3v-8h-2v-3h2v-1.923c0-2.022 1.064-3.077 3.461-3.077h2.539v3z"
              />
            </svg>
            <svg class="expand mx-1" width="48" height="48" viewBox="0 0 48 48">
              <path
                d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"
              />
            </svg>
            <svg class="expand mx-1" width="48" height="48" viewBox="0 0 48 48">
              <path
                d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"
              />
            </svg>
          </div>
          <div class="col-md-6 col-sm-12 mx-auto">
            <h3>Contacto</h3>
            <hr width="90%" />
            <b-form id="contacto" @submit="onSubmit" @reset="onReset">
              <b-form-group
                id="input-contacto-group-1"
                label="Email:"
                label-for="input-contacto-1"
                description="Nunca compartiremos su correo electrónico con nadie más."
              >
                <b-form-input
                  id="input-contacto-1"
                  v-model="form.email"
                  type="email"
                  required
                  placeholder="Ingrese email"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-contacto-group-2"
                label="Tu Nombre:"
                label-for="input-contacto-2"
              >
                <b-form-input
                  id="input-contacto-2"
                  v-model="form.name"
                  required
                  placeholder="Ingrese su nombre"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-contacto-group-3"
                label="Asunto:"
                label-for="input-contacto-3"
              >
                <b-form-input
                  id="input-contacto-3"
                  v-model="form.asunto"
                  required
                  placeholder="Ingrese el asunto"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-contacto-group-4"
                label="Mensaje:"
                label-for="input-contacto-4"
              >
                <b-form-textarea
                  id="input-contacto-4"
                  v-model="form.msj"
                  placeholder="Ingrese el mensaje..."
                  rows="3"
                  max-rows="6"
                ></b-form-textarea>
              </b-form-group>

              <b-button class="mx-1" type="submit" variant="primary"
                >Enviar</b-button
              >
              <b-button class="mx-1" type="reset" variant="danger"
                >Limpiar</b-button
              >
            </b-form>
            <hr width="90%" />
          </div>
        </div>
        <div class="mx-auto text-center">
          <small>Copyright &copy; JhojaForce Company</small>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import { myMixins } from "@/mixins.js";

export default {
  name: "App",
  data() {
    return {
      sCroll: false,
      showBt: false,
      form: {
        email: "",
        name: "",
        asunto: "",
        msj: ""
      }
    };
  },
  mixins: [myMixins],
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.name = "";
      this.form.asunto = "";
      this.form.msj = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    handleSCroll(event) {
      if (window.scrollY > 100) {
        this.sCroll = true;
      } else {
        this.sCroll = false;
      }
      if (window.scrollY > 900) {
        this.showBt = true;
      } else {
        this.showBt = false;
      }
    }
  },
  created() {
    window.addEventListener("scroll", this.handleSCroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleSCroll);
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  min-height: 650px;
}
.page-content {
  flex: 1 0 auto;
}
#sticky-footer {
  flex-shrink: none;
}
.expand {
  -webkit-transform: scale(1.3);
  -ms-transform: scale(1.3);
  transform: scale(1.3);
}
.delay-1s {
  animation-duration: 1s;
}
.slide-leave-active,
.slide-enter-active {
  transition: opacity 1s, transform 1s;
}
.slide-enter,
.slide-leave-to {
  opacity: 0;
  transform: translate(-30%, 0);
}
</style>
