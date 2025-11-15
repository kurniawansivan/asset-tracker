<script lang="ts">
	import { onMount } from 'svelte';

    interface Asset {
        id: number;
        name: string;
        serial_number: string | null;
        purchase_date: string; 
        wwarranty_expires: string | null;
    }

	let assets: Asset[];

    let name = '';
    let serial_number = '';
    let purchase_date = '';
    let warranty_expires = '';

	onMount(async () => {
		const response = await fetch('http://localhost:8000/api/assets/');
		const data = await response.json();
		assets = data;
	});

    async function handleSubmit(){
        console.log("Form submitted");
        console.log({name, serial_number, purchase_date, warranty_expires});
    }
</script>

<h1>Welcome to Aegis</h1>

<form on:submit|preventDefault={handleSubmit}>
    <div>
        <label for="name">Asset Name</label>
        <input type="text" id="name" name="name" required bind:value={name}/>
    </div>

    <div>
        <label for="serial_number">Serial Number</label>
        <input type="text" id="serial_number" name="serial_number" bind:value={serial_number}/>
    </div>

    <div>
        <label for="purchase_date">Purchase Date</label>
        <input type="date" id="purchase_date" name="purchase_date" required bind:value={purchase_date}/>
    </div>

    <div>
        <label for="warranty_expires">Warranty Expires</label>
        <input type="date" id="warranty_expires" name="warranty_expires" bind:value={warranty_expires}/>
    </div>

    <button type="submit">Add Asset</button>
</form>

{#each assets as asset}
  <div>
    <h2>{asset.name}</h2>
    <p>Serial Number: {asset.serial_number}</p>
    <p>Purchase Date: {asset.purchase_date}</p>
  </div>
{/each}