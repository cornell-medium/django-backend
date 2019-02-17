class Tag(models.Model)
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag