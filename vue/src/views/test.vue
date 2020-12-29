<template>
    <div class="d-flex flex-column justify-content-center align-items-center" style="height: 80vh">
        <div class="p-2">
            <h1 v-if="!APIResult.length"> If no result Click </h1>
            <h1 v-else style="font-size:4rem"> {{ APIResult }}</h1>
            <button v-if="!APIResult.length"
                @click="test"
                type="button"
                class="btn btn-primary btn-lg btn-block">Here </button>
        </div>
    </div>
</template>


<script>
import { getAPI } from "@/axios";
export default {
    name: "test",
    data() {
        return {
            testdata: "hello",
            APIResult: []
    };
},
methods: {
    test() {
        getAPI
            .get("/test",{
                params:{
                    test: this.testdata
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