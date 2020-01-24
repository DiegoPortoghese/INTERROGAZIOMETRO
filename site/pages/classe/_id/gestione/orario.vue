<template>
<main>
    <div class="nav-scroller bg-white box-shadow">
      <nav class="nav nav-underline">
        <a class="nav-link" href="../gestione/">Principale</a>
        <a class="nav-link" href="#">Note</a>
        <a class="nav-link active" href="../gestione/orario">Orario</a>
        <a class="nav-link" href="../gestione/interrogazioni">Interrogazioni</a>
        <a class="nav-link" href="../gestione/conferme">
          Conferme
          <span class="badge badge-pill bg-light align-text-bottom"></span>
        </a>
      </nav>
    </div>
<CalendarManager :calendarEvents="calendarEvents" :classeId="classe.id"/>
</main>
</template>

<script>

let components = {};
if(process.browser) {
    const CalendarManager = require('~/components/CalendarManager').default;
    components = {
        CalendarManager
    }
}

export default {
    components ,
    mounted() {
      //this.asyncData()
      this.$nextTick(function () {
        this.onResize();
      })
      window.addEventListener('resize', this.onResize)
      
      this.setCalendarEvents()
    },
    async asyncData({ $axios, params }) {
      try {
        let classe = await $axios.$get(`api/classe/${params.id}/`);
        return { classe };
      } catch (e) {
        return { classe: [] };
      }
    },
    data() {
      return {
          classe: {
            sezione: '',
            anno:0,
            nome: "",
            descrizione: "",
          },
          calendarEvents: [],
          isNotMobile: false
          }
      },
    methods:{
      onResize() {
          this.isNotMobile = document.documentElement.clientWidth > 1600;
          console.log(document.documentElement.clientWidth)
        },

      setCalendarEvents(){
        let cls = this.classe
        for (let key in cls.orario){
          var object = cls.orario[key]
          this.calendarEvents.push(
                {
                  groupId: object.id,
                  daysOfWeek: [ (object.giorno_della_settimana).toString() ],
                  startTime: (object.numero_ora).toString()+':00:00',
                  endTime: (object.numero_ora+1).toString()+':00:00',
                  title: object.materia_nome
                }
          )
        }
        console.log(this.calendarEvents)
      }


    }
  }
</script>