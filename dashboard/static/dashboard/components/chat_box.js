const chatBox = Vue.component('chat-box', {
    delimiters: ['[[', ']]'],
    props: ['user_pk', 'is_coach', 'user_name'],
    data: function () {
        return {
            chat_data: [],
            chatSocket: '',
            chatDisplay: false,
            requestedUserName: "Chat",
        }
    },
    async created() {
        await this.get_chat_data(); 
    },
    async mounted(){
        var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
        this.chatSocket = new WebSocket(ws_scheme + '://' + window.location.host + '/ws/notification/');
        let chatComponent = this;
        this.chatSocket.onmessage = async function(e) {
            await chatComponent.get_chat_data(); 
        };
    },
    methods: {
        async get_chat_data() {
            if (this.user_pk != ''){
                var response = await fetch('https://business-coaching.herokuapp.com/api/chat/' + String(this.user_pk) + '/');
                this.chat_data = await response.json();
            }
        },
        async send_message() {
            var url = 'https://business-coaching.herokuapp.com/api/chat/';
            var msg = String(document.getElementById("input_message").value).replace(/(\r\n|\n|\r)/gm, "")
            console.log(msg);
            await fetch(url, {
                method: 'post',
                headers: {
                'X-CSRFTOKEN' : get_cookie('csrftoken'),
                'Content-Type': 'application/json'
                },
                body:JSON.stringify({
                    "pk": parseInt(this.user_pk),
                    "message" : msg
                })
            });
            document.getElementById("input_message").value = ""
            await this.get_chat_data();
        },
        toggleDisplay: function(){
            this.chatDisplay = !this.chatDisplay
        }
    },
    template: `<div id="selected_chat" class="container floating_chat" style="position:relative; z-index:1000">
                    <div class="row" style="float: right; width: 375px; position:fixed;right:40px;bottom:1%;">
                        <div class="card">
                           <div v-on:click="toggleDisplay()" class="card-header" style="float: right; width: 350px; cursor:pointer">[[ requestedUserName ]]</div>
                                <div v-show="chatDisplay" id="chat-messages" style="background-color:#e6ffff; ">
                                    <ul class="chat-list" style="width: 350px; height:400px;overflow:auto; display: flex; flex-direction: column-reverse;">
                                        <div v-for="chat in chat_data" :key="chat.pk">
                                            <li v-if='user_pk == chat.sender.pk' class="in">
                                                <div class="chat-img">
                                                    <img alt="Avatar" :src="[[ chat.sender.profile_photo ]]">
                                                </div>
                                                <div class="chat-body">
                                                    <div class="chat-message">
                                                        <h5>[[ chat.sender.first_name ]] [[ chat.sender.last_name ]]</h5>
                                                        <p>[[ chat.message ]]</p>
                                                    </div>
                                                </div>
                                            </li>
                                            <li v-else class="out">
                                                <div class="chat-img">
                                                    <img alt="Avatar" :src="[[ chat.sender.profile_photo ]]">
                                                </div>
                                                <div class="chat-body">
                                                    <div class="chat-message">
                                                        <h5>[[ chat.sender.first_name ]] [[ chat.sender.last_name ]]</h5>
                                                        <p>[[ chat.message ]]</p>
                                                    </div>
                                                </div> 
                                            </li> 
                                        </div> 
                                    </ul>
                                    <div class="form-group mt-3 mb-0">
                                        <textarea v-on:keyup.enter="send_message()" class="form-control" id="input_message" rows="1"  placeholder="Type your message here..."></textarea>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
    `,
    watch: { 
        user_pk: function(new_user_pk, old_user_pk) { // watch it
            this.get_chat_data();
            this.chatDisplay = true;
        },
        user_name: function(new_user_name, old_user_name) { // watch it
            this.requestedUserName = new_user_name;
            this.chatDisplay = true; 
        }
    }
})
