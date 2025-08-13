<script lang="ts">
	import { page } from "$app/state";
    import Sidebar from "$lib/components/layout/Sidebar/Sidebar.svelte";
	import { Button } from "$lib/components/ui";

</script>

<main>

    <Sidebar/>
    <section>
        <Button
        
        >
        CLique
    </Button>
    </section>
    
</main>

<style>
    main {
        display: flex;
    }
</style>
