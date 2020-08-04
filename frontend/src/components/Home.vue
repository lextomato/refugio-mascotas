<template>
  <div>
    <header>
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        background="#ababab"
        img-width="1370"
        img-height="451"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
        class="animate__animated animate__zoomInUp"
      >
        <!-- Text slides with image -->
        <b-carousel-slide
          caption="First slide"
          text="Nulla vitae elit libero, a pharetra augue mollis interdum."
        >
          <template v-slot:img>
              <img
                class="d-block img-fluid w-100"
                width="1370"
                height="451"
                src="@/assets/slide1.jpg"
                alt="image slot"
              >
          </template>
        </b-carousel-slide>

        <!-- Slides with custom text -->
        <b-carousel-slide>
          <h1 class="animate__animated animate__zoomInDown">Hello world!</h1>
          <template v-slot:img>
              <img
                class="d-block img-fluid w-100"
                width="1370"
                height="451"
                src="@/assets/slide2.jpg"
                alt="image slot"
              >
          </template>
        </b-carousel-slide>

        <!-- Slides with img slot -->
        <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
        <b-carousel-slide>
          <template v-slot:img>
            <img
              class="d-block img-fluid w-100"
              width="1370"
              height="451"
              src="@/assets/slide3.jpg"
              alt="image slot"
            >
          </template>
        </b-carousel-slide>
      </header>

      <!-- Page Content -->
      <div class="container mt-4" @scroll="handleSCrollHome">

        <h1 class="my-5 animate__animated animate__zoomInDown delay-1s">Bienvenidos a CasaAdoptiva.org</h1>
        <br>
        <hr width="90%" />
        <br>

        <b-modal id="modal-center" size="lg" class="bg-light" centered title="BootstrapVue">
          <template v-slot:modal-header="{ close }">
            <!-- Emulate built in modal header close button action -->
            <b-button size="sm" variant="outline-danger" @click="close()">
              Cerrar
            </b-button>
            <h4>{{ selectedItem.nombre }}</h4>
          </template>

            <div class="row">
              <div class="col-md-5 col-sm-12">
                <b-img
                  class="modal-img-profile"
                  fluid
                  v-bind="mainProps"
                  rounded="circle"
                  :src="selectedItem.foto"
                  alt="Circle image"
                ></b-img>
              </div>
              <div class="col-md-7 col-sm-12">
                <div class="row my-3">
                  <div class="container text-center">
                    <p class="text-muted"><b-icon class="card-text" icon="calendar-date" aria-hidden="true"></b-icon>
                    Rescatado: {{ selectedItem.fecha_rescate }} | 
                    <b-icon class="card-text" icon="clock-history" aria-hidden="true"></b-icon>
                    {{ selectedItem.edad_aproximada }} Años | 
                    <svg width="18" height="18" viewBox="0 0 24 24">
                      <path
                        d="M16 0v2h2.586l-2.113 2.113c-.981-.698-2.177-1.113-3.473-1.113-2.22 0-4.144 1.216-5.18 3.009-3.229.096-5.82 2.738-5.82 5.991 0 2.973 2.164 5.433 5 5.91v2.09h-3v2h3v2h2v-2h3v-2h-3v-2.09c1.791-.301 3.294-1.403 4.167-2.918 3.235-.09 5.833-2.735 5.833-5.992 0-1.296-.415-2.492-1.113-3.473l2.113-2.113v2.586h2v-6h-6zm-3 13c-1.944 0-3.564-1.396-3.923-3.236-.66-.333-1.365-.346-2.033-.066.266 2.293 1.827 4.181 3.931 4.938-.729.831-1.784 1.364-2.975 1.364-2.206 0-4-1.794-4-4s1.794-4 4-4c1.937 0 3.555 1.384 3.921 3.214.679.35 1.309.383 2.033.077-.27-2.293-1.837-4.179-3.943-4.931.732-.83 1.797-1.36 2.989-1.36 2.206 0 4 1.794 4 4s-1.794 4-4 4z"
                      />
                    </svg>
                    {{ selectedItem.sexo | capitalize }} </p>
                    <p class="text-muted">Especie: <b-badge>{{ selectedItem.especie }}</b-badge>   |   Raza: <b-badge>{{ selectedItem.raza }}</b-badge></p>
                  </div>
                </div>
                <hr width="90%" />
                <div class="row my-3">
                  <div class="container">
                    <h5>Sobre <strong>{{ selectedItem.nombre }}</strong>:</h5>
                    <br>
                    <p class="text-justify">{{ selectedItem.reseña }}</p>
                  </div>
                </div>
              </div>
            </div>

          <template v-slot:modal-footer>
            <b-button v-if="!selectedItem.persona" :to="{ name: 'Solicitud', params: { tipo: 'Adoptante', mascotaId: selectedItem.id }}" size="sm" variant="info">Adoptar</b-button>
            <b-button v-else size="sm" variant="info" disabled>Adoptar</b-button>
          </template>
        </b-modal>

        <div class="card bg-dark text-white border-0 shadow-lg">
          <img style="max-height: 300px" src="@/assets/grid-adopt.jpg" class="card-img" alt="...">
          <div class="card-img-overlay">
            <div class="row">
              <div class="col-2"></div>
              <div class="col-9">
                <h2>Sin Hogar de esta semana</h2>
                <small>ADOPTA!</small>
                <div class="row">
                  <b-col cols="3" v-for="mascota in listado4" :key="mascota.id">
                    <transition name="bounce">
                      <div v-show="showAdoptar">
                        <b-img v-b-modal.modal-center @click="sendInfo(mascota)" class="img-hover card-img-profile mb-2" fluid v-bind="mainProps" rounded="circle" :src="mascota.foto" alt="Circle image"></b-img>
                        <br>{{ mascota.nombre }}
                        <br><router-link class="text-muted" :to="{ name: 'Solicitud', params: { tipo: 'Adoptante', mascotaId: mascota.id }}"><b-icon role="button" variant="primary" animation="throb" icon="bookmark-plus" aria-hidden="true"></b-icon></router-link>
                            <small class="text-muted">Adoptar</small>
                      </div>
                    </transition>
                  </b-col>
                </div>
              </div>
              <div href="/mascotas" class="col-1 d-flex align-content-center flex-wrap text-center selected rounded-lg">
                <transition name="bounce">
                  <div v-show="showAdoptar">
                    <router-link to="/mascotas">
                    <b-icon role="button" font-scale="2" variant="info" class="rounded-lg" icon="grid3x3-gap"></b-icon>
                    </router-link>
                    <br><p>Ver
                    Todos</p>
                  </div>
                </transition>
              </div>
            </div>
          </div>
        </div>
        
        <br>
        <hr width="90%" />
        <br>

        <div class="card bg-light text-dark border-0 shadow-lg">
          <img style="max-height: 612px" src="@/assets/grid-noticias.jpg" class="card-img" alt="...">
          <div class="card-img-overlay">
            <div class="row">
              <div class="col-6">
                <h2>Noticias Comunidad</h2>
                <hr width="90%" />
                <div class="row justify-content-md-center">
                  <b-col cols="12">

                      <div :class="[ showNoticias ? 'animate__backInRight': 'animate__backOutRight' ]" class="animate__animated">
                        <div class="mx-auto mt-5 bg-light text-dark card mb-3 shadow rounded-pill-l" style="max-width: 540px;">
                          <div class="row no-gutters">
                            <div class="col-md-9">
                              <img :src="noticias[0].img_portada" class="shadow rounded-pill-l card-img sticky-card-img" alt="...">
                              <p class="card-title mt-2 ml-5 pl-3 font-weight-bold">{{ noticias[0].titulo }}</p>
                            </div>
                            <div class="col-md-3 d-flex align-content-center flex-wrap text-center">
                              <div class="card-body px-2">
                                <p class="card-text"><small class="text-muted"><b-icon icon="clock"></b-icon> {{ noticias[0].fecha | transcurrido }}</small></p>
                                <p class="card-text"><small class="rounded-lg text-white bg-secondary shadow-sm"><b-icon icon="hash"></b-icon>{{ noticias[0].categoria }} |</small></p>
                                <p class="card-text text-muted"><b-icon icon="file-text"></b-icon> Ver <router-link :to="{ name: 'noticia-detail', params: { noticiaId: noticias[0].id }}"><b-icon role="button" class="bt-hover" icon="box-arrow-in-right" variant="primary"></b-icon></router-link></p>
                              </div>
                            </div>
                          </div>
                        </div>
                        <hr width="90%" />
                        <div class="mx-auto mt-5 bg-light text-dark card mb-2 shadow rounded-pill-l" style="max-width: 540px;">
                          <div class="row no-gutters">
                            <div class="col-md-9">
                              <img :src="noticias[1].img_portada" class="shadow rounded-pill-l card-img sticky-card-img" alt="...">
                              <p class="card-title mt-2 ml-5 pl-3 font-weight-bold">{{ noticias[1].titulo }}</p>
                            </div>
                            <div class="col-md-3 d-flex align-content-center flex-wrap text-center">
                              <div class="card-body px-2">
                                <p class="card-text"><small class="text-muted"><b-icon icon="clock"></b-icon> {{ noticias[1].fecha | transcurrido }}</small></p>
                                <p class="card-text"><small class="rounded-lg text-white bg-secondary shadow-sm"><b-icon icon="hash"></b-icon>{{ noticias[1].categoria }} |</small></p>
                                <p class="card-text text-muted"><b-icon icon="file-text"></b-icon> Ver <router-link :to="{ name: 'noticia-detail', params: { noticiaId: noticias[1].id }}"><b-icon role="button" class="bt-hover" icon="box-arrow-in-right" variant="primary"></b-icon></router-link></p>
                              </div>
                            </div>
                          </div>
                        </div>
                        <hr width="90%" />
                      </div>

                  </b-col>
                  <b-col style="max-height: 45px; max-width: 50%;" cols="12" class="px-0 pb-0 pt-1 selected rounded-lg">
                    <router-link class="text-dark" to="/noticias-comunidad"><p><b-icon role="button" font-scale="2" variant="info" class="rounded-lg" icon="archive"></b-icon> Más noticias</p></router-link>
                  </b-col>
                </div>
              </div>
              <div class="col-6"></div>
            </div>
          </div>
        </div>

        <br>
        <hr width="90%" />
        <br>
        
        <div class="card bg-light text-dark border-0 shadow-lg mb-3">
          <img style="max-height: 612px" src="@/assets/padrino.jpg" class="card-img" alt="...">
          <div class="card-img-overlay">
            <div class="row">
              <div class="col-7"></div>
              <div class="col-5">
                <div :class="[ showPadrino ? 'animate__backInUp': 'animate__backOutDown' ]" class="card bg-light p-3 my-auto shadow-lg animate__animated">
                  <h2>Conviértete en Padrino!</h2>
                  <hr width="90%" />
                  <div class="row justify-content-md-center">
                    <b-col cols="12">

                        Click en el botón y llena el formulario con tus y de la mascota

                        <hr width="90%" />
                          <b-button :to="{ name: 'Solicitud', params: { tipo: 'Padrino', mascotaId: selectedItem.id }}" block pill size="lg" variant="outline-primary">Click aquí!</b-button>
                        <hr width="90%" />

                    </b-col>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
      <!-- /.container -->
  </div>
</template>

<script>
import {myMixins} from '@/mixins.js'

export default {
  name: 'Home',
  data () {
    return {
      mascotas: [],
      listado4: [],
      noticias: [],
      showAdoptar: false,
      showNoticias: false,
      showPadrino: false,
      selectedItem: [],
      categoria: []
    }
  },
  filters: {
    transcurrido: function (value) {
      let resp = ''
      let inicio = Date.parse(value)
      inicio = new Date(inicio)
      let fin = Date.now()
      let transcurso = fin -inicio
      if (transcurso < 86400000) {
        resp = 'Hoy'
      } else if (transcurso >= 86400000 && transcurso < 86400000*2) {
        resp = 'Hace 1 día'
      } else if (transcurso >= 86400000*2 && transcurso < 86400000*30) {
        resp = 'Hace ' + Math.floor(transcurso/86400000) + ' días'
      } else if (transcurso >= 86400000*30 && transcurso < 86400000*30*2) {
        resp = 'Hace 1 mes'
      } else if (transcurso >= 86400000*30*2 && transcurso < 86400000*30*12) {
        resp = 'Hace ' + Math.floor(transcurso/(86400000*30)) + ' meses'
      } else if (transcurso >= 86400000*30*12 && transcurso < 86400000*30*12*2) {
        resp = 'Hace 1 año'
      } else {
        resp = 'Hace ' + Math.floor(transcurso/(86400000*30*12)) + ' años'
      }
      return resp
    }
  },
  mixins: [myMixins],
  methods: {
      sendInfo(item) {
        this.selectedItem = item
        this.selectedItem.especie = this.categoria[this.selectedItem.categoria - 1].especie
        this.selectedItem.raza = this.categoria[this.selectedItem.categoria - 1].raza
      },
      handleSCrollHome (event) {
        if (window.scrollY > 350) {
          this.showAdoptar = true
        } else {
          this.showAdoptar = false
        }
        if (window.scrollY > 770) {
          this.showNoticias = true
        } else {
          this.showNoticias = false
        }
        if (window.scrollY > 1200) {
          this.showPadrino = true
        } else {
          this.showPadrino = false
        }
      }
    },
  created () {
    this.scrollBehavior(),
    this.getMascotas(),
    this.getCategoria(),
    this.getNoticias(),
    window.addEventListener('scroll', this.handleSCrollHome)
  },
  destroyed () {
    window.removeEventListener('scroll', this.handleSCrollHome)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .selected:hover {
    background-color: rgba(0,0,0,0.2);
    transition-property: background-color;
    transition-duration: .20s;
  }
  .img-hover:hover
    {
      transition-property: transform;
      transition-duration: .20s;
      -webkit-transform: scale(1.6);
      -ms-transform: scale(1.6);
      transform: scale(1.6);
      position: relative;
      z-index: 10;
    }
  .card-img-profile {
    border: 5px solid #f7f7f7;
    max-width: 70%;
  }
  .bounce-enter-active {
    animation: bounce-in .5s;
  }
  .bounce-leave-active {
    animation: bounce-in .5s reverse;
  }
  @keyframes bounce-in {
    0% {
      transform: scale(0);
    }
    50% {
      transform: scale(1.5);
    }
    100% {
      transform: scale(1);
    }
  }
  .sticky-card-img {
    margin-top: -45px;
    margin-left: 10px;
    max-height: 160px;
    height: 100%;
    width: 100%;
    display: block;
    object-fit: cover;
    object-position: center center;
  }
  .rounded-pill-l {
    border-radius: 50rem 2rem 2rem 50rem!important;
  }
  .bt-hover:hover
    {
        transition-property: transform;
        transition-duration: .20s;
        -webkit-transform: scale(1.8);
        -ms-transform: scale(1.8);
        transform: scale(1.8);
    }
    .delay-1s {
      animation-duration: 1s
    }
</style>
