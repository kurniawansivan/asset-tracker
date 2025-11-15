<script lang="ts">
	import { onMount } from 'svelte';

	let assets = [];

	onMount(async () => {
		const response = await fetch('/api/assets');
		const data = await response.json();
		assets = data;
	});
</script>

<h1>Welcome to Aegis</h1>
