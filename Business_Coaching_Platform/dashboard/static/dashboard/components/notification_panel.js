const notificationPanel = Vue.component('notification-panel', {
    delimiters: ['[[', ']]'],
    props: ['user_pk'],
    data: function () {
        return {
            notificationData: '',
            notificationNumber: 0,
            socket: '',
            hover: false
        }
    },
    async created() {
        await this.get_notification_data(); 
    },
    async mounted(){
        this.socket = new WebSocket('ws://' + window.location.host + '/ws/notification/');
        let notificationComponent = this;
        this.socket.onmessage = async function(e) {
            await notificationComponent.get_notification_data(); 
        };
    },
    methods: {
        async get_notification_data() {
            var response = await fetch('http://localhost:8000/api/notification/');
            this.notificationData = await response.json();
            this.notificationNumber = this.notificationData.length
        },
        async clear_all_notification() {
            var len = this.notificationData.length
            for (var i = 0; i < len; i++) {
                await this.clear_notification(this.notificationData[i].pk);
            }
            await this.get_notification_data();
        },
        async clear_notification(pk) {
            var url = 'http://localhost:8000/api/notification/';
            await fetch(url, {
                method: 'delete',
                headers: {
                    'X-CSRFTOKEN': get_cookie('csrftoken'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "pk": String(pk)
                })
            });
        }
    },
    template: `
            <div class="notification">
                <a class="fa fa-bell"></a>
                <span v-if='notificationNumber > 0' class="badge" > [[ notificationNumber ]]</span>
                <div class="notification-content">
                    <li v-for="notification in notificationData" :key="notification.pk" v-if="notification.receiver.pk == user_pk" class="notification-box">
                        <div class="row" style="margin-left:-15px; margin-right:0px;">
                          <div class="col-lg-3 col-sm-3 col-3 text-center">
                            <img :src="notification.sender.profile_photo" class="w-75 rounded-circle">
                          </div>    
                          <div class="col-lg-8 col-sm-8 col-8">
                            <strong class="text-info">[[ notification.sender.name]]</strong>
                            <div>
                                [[ notification.event ]]
                            </div>
                          </div>    
                        </div>
                    </li>
                    <a v-if='notificationNumber > 0' v-on:click="clear_all_notification()" class="clear-all-btn"> &nbsp; &nbsp;&nbsp; &nbsp; Clear all</a>
                </div>
            </div>
    `,
    watch: { 
    }
})
