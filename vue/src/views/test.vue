<template>
    <div class="d-flex flex-column justify-content-center align-items-center" style="height: 80vh">
        <div class="p-2">
            <input v-if="!APIResult.length" v-model="message" placeholder="enter numbers">
            <h1 v-if="!APIResult.length">  </h1>
            <h1 v-else style="font-size:4rem"> {{ APIResult }}</h1>
            <button v-if="!APIResult.length"
                @click="test"
                type="button"
                class="btn btn-primary btn-lg btn-block"> Bubble Sort </button>
        </div>
    </div>
</template>

<script>
import { getAPI } from "@/axios";
export default {
    name: "test",
    data() {
        return {
            testdata: "hellofromvue-goto-flask-comeback",
            APIResult: [],
            text: '',
            message: ''
    };
},
methods: {
    test() {
        getAPI
            .get("/test",{
                params:{
                    inputdata: this.message
                    }
                })
                .then(response => {
                    console.log("recived");
                    this.APIResult = response.data;
                    console.log(response.data);
                })
                .catch(err => {
                    console.log(err);
                });
            }
        }
    };
</script>
