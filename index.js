
async function signInWithEmail() {
  const { data, error } = await supabase.auth.signInWithOtp({
    email: (username),
    options: {
      emailRedirectTo: 'https://viper-net.vercel.app/',
    },
  })
}
