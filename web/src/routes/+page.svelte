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

	onMount(async () => {
		const response = await fetch('http://localhost:8000/api/assets');
		const data = await response.json();
		assets = data;
	});
</script>

<h1>Welcome to Aegis</h1>

{#each assets as asset}
  <div>
    <h2>{asset.name}</h2>
    <p>Serial Number: {asset.serial_number}</p>
    <p>Purchase Date: {asset.purchase_date}</p>
  </div>
{/each}