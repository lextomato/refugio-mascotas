import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/components/Home";
import About from "@/components/About";
import Login from "@/components/Login";

import ListMascota from "@/components/Mascota/ListMascota";
import Solicitud from "@/components/Mascota/Solicitud";
import ListNoticias from "@/components/Noticias/ListNoticias";
import NoticiaDetail from "@/components/Noticias/NoticiaDetail";

import Dashboard from "@/components/Administrar/Dashboard";
import preSolicitud from "@/components/Administrar/Solicitudes/preSolicitud";
import Error404 from "@/components/Error404";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: { Auth: false, title: 'Home' }
  },
  {
    path: "/Nosotros",
    name: "About",
    component: About,
    meta: { Auth: false, title: 'About' }
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: { Auth: false, title: 'Login' },
      beforeEnter: (to, from, next) => {
          // Si existe un token, la sesion existe, por lo cual, redirecciona a home
          // if (window.localStorage.getItem('_token')) {
          if (!!localStorage.getItem('token')) {
            next({ path: '/' });
          } else {
            next();
          }
      },
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: { Auth: true, title: 'Escritorio' }
  },
  {
    path: "/dashboard/presolicitud=:preSolicitudId",
    name: "preSolicitud",
    component: preSolicitud,
    meta: { Auth: true, title: 'Pre-Solicitud' }
  },
  {
    path: "/mascotas",
    name: "ListMascota",
    component: ListMascota,
    meta: { Auth: false, title: 'Mascotas' }
  },
  {
    path: "/mascotas/solicitud",
    name: "Solicitud",
    component: Solicitud,
    meta: { Auth: false, title: 'Solicitud' }
  },
  {
    path: "/mascotas/solicitud=:tipo/:mascotaId",
    name: "Solicitud",
    component: Solicitud,
    meta: { Auth: false, title: 'Solicitud' }
  },
  {
    path: "/noticias-comunidad",
    name: "ListaNoticias",
    component: ListNoticias,
    meta: { Auth: false, title: 'Noticias' }
  },
  {
    path: "/noticias-comunidad/search=:word",
    name: "ListaNoticias",
    component: ListNoticias,
    meta: { Auth: false, title: 'Noticias' }
  },
  {
    path: "/noticias-comunidad/:noticiaId",
    name: "noticia-detail",
    component: NoticiaDetail,
    meta: { Auth: false, title: 'Noticia-Detail' }
  },
  {
    path: "/404",
    name: "Error-404",
    component: Error404,
    meta: { Auth: false, title: '404' }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
  // scrollBehavior() {
  //   return {x: 0, y: 0}
  // }
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  if (to.meta.Auth && !localStorage.getItem('token')) {
    next({ path: '/login' });
  } else {
    next();
  }
});

export default router;
