<script lang="ts">
    import '../styles/global.scss';
    import type { LayoutProps } from './$types';
    let {children }: LayoutProps = $props();
</script>

{@render children()}