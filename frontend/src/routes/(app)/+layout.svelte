<!-- src/routes/+layout.svelte -->
<script>
    let { children } = $props();
</script>

{@render children()}
