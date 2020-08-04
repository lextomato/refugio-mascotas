import axios from "axios";

export const myMixins = {
  methods: {
    scrollBehavior() {
      window.scrollTo({ top: 0 });
    },
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
    getMascotas() {
      const path = "http://localhost:8000/api/v1.0/mascota/all";
      axios
        .get(path)
        .then(response => {
          this.loading = false;
          this.mascotas = response.data;

          let listado = [];
          for (let i = 0; i < this.mascotas.length; i++) {
            if (!this.mascotas[i].persona) {
              listado[i] = this.mascotas[i];
            }
          }
          listado = this.filtroNuloRepetido(listado);
          let aleatorio = 0;
          for (let i = 0; i < 4; i++) {
            aleatorio = Math.floor(Math.random() * listado.length);
            this.listado4[i] = listado[aleatorio];
            listado.splice(aleatorio, 1);
            listado = this.filtroNuloRepetido(listado);
          }
          this.listado4 = this.filtroNuloRepetido(this.listado4);
        })
        .catch(error => {
          console.log(error);
        });
    },
    getCategoria() {
      const path = "http://localhost:8000/api/v1.0/mascota/categoria/";
      axios
        .get(path)
        .then(response => {
          this.categoria = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getVacunas() {
      const path = "http://localhost:8000/api/v1.0/mascota/vacuna/";
      axios
        .get(path)
        .then(response => {
          this.vacunas = response.data;
          for (let i = 0; i < this.vacunas.length; i++) {
            this.vacunas[i] = {
              value: this.vacunas[i].id,
              text: this.vacunas[i].nombre
            };
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    getNoticias() {
      const path = "http://localhost:8000/api/v1.0/noticias/";
      axios
        .get(path)
        .then(response => {
          this.loading = false;
          this.noticias = response.data;
          this.noticias.sort(function(a, b) {
            return (
              new Date(Date.parse(b.fecha)) - new Date(Date.parse(a.fecha))
            );
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    getPreSolicitud() {
      const path = "http://localhost:8000/api/v1.0/adopcion/pre-solicitud-administrar/";
      axios
        .get(path)
        .then(response => {
          this.items = response.data;
          this.totalRows = this.items.length
        })
        .catch(error => {
          console.log(error);
        });
    },
    getSolicitud() {
      const path = "http://localhost:8000/api/v1.0/adopcion/solicitud/";
      axios
        .get(path)
        .then(response => {
          this.items2 = response.data;
          this.totalRows2 = this.items2.length
        })
        .catch(error => {
          console.log(error);
        });
    },
    getPersonas() {
      const path = "http://localhost:8000/api/v1.0/adopcion/personas/";
      axios
        .get(path)
        .then(response => {
          this.personas = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    filtroNuloRepetido(obj) {
      obj = obj.filter(function(el) {
        return el != null;
      });
      obj = obj.filter((valorActual, indiceActual, arreglo) => {
        return (
          arreglo.findIndex(
            valorDelArreglo =>
              JSON.stringify(valorDelArreglo) === JSON.stringify(valorActual)
          ) === indiceActual
        );
      });
      return obj;
    },
    buscarEnObjecto(obj, palabras) {
      let aux = 0;
      for (let key in obj) {
        if (key != "persona" && key != "padrino" && key != "vacuna") {
          for (let i = 0; i < palabras.length; i++) {
            if (
              obj.hasOwnProperty(key) &&
              obj[key]
                .toString()
                .toLowerCase()
                .includes(palabras[i])
            ) {
              aux++;
            }
          }
        }
      }
      if (aux >= palabras.length) {
        return true;
      }

      return false;
    },
    searchFilt(obj) {
      let palabras = this.searchText.toLowerCase();
      palabras = this.words(palabras);
      return obj.filter(item => {
        return this.buscarEnObjecto(item, palabras);
      });
    },
    words(searchText) {
      let array = searchText.split(" ");
      array = array.filter(function(el) {
        return el != "";
      });
      return array;
    },
    filtDisp(filtrados) {
      if (this.filtros.disp) {
        let aux = [];
        for (let i = 0; i < filtrados.length; i++) {
          if (!filtrados[i].persona) {
            aux[i] = filtrados[i];
          }
        }
        if (aux != []) {
          filtrados = aux;
        }

        filtrados = this.filtroNuloRepetido(filtrados);
      }
      return filtrados;
    },
    logoutSession () {
      axios.post(this.$store.state.endpoints.logoutJWT, {
        headers: {
            // Set your Authorization to 'JWT', not Bearer!!!
              Authorization: `JWT ${this.$store.state.jwt}`,
              'Content-Type': 'application/json'
            }
      })
        .then((response) => {
          this.$store.commit('removeToken', response.data.token)
          this.$store.commit("setAuthUser",
                {authUser: {}, isAuthenticated: false}
              )
          this.$swal.fire(
            'Cierre de sesión exitoso!',
            'Presiona ok!',
            'success'
          )
          this.$router.push({name: 'Home'})
        })
        .catch((error) => {
          this.$swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'error interno',
          })
          console.log(error);
          console.debug(error);
          console.dir(error);
        })
    },
    objToFormData (obj) {
      function buildFormData(formData, data, parentKey) {
        if (
            data &&
            typeof data === "object" &&
            !(data instanceof Date) &&
            !(data instanceof File)
            ) {
                Object.keys(data).forEach(key => {
                    buildFormData(
                        formData,
                        data[key],
                        parentKey ? `${parentKey}[${key}]` : key
                    );
                });
            } else {
                const value = data == null ? "" : data;
                formData.append(parentKey, value);
            }
        }

      function jsonToFormData(data) {
          const formData = new FormData();
          buildFormData(formData, data);
          return formData;
      }

      let aux = jsonToFormData(obj)

      return aux
    },
    dataURLtoBlob( dataUrl, callback ) {
        let req = new XMLHttpRequest;

        req.open( 'GET', dataUrl );
        req.responseType = 'blob';

        req.onload = function fileLoaded(e)
          {
            callback(this.response);
          };

          req.send();
    }
  }
};
